import numpy as np

class Homographer():
    def __init__(self, pts_src, pts_dst):
        self.h = None

        self.src1 = pts_src[0]
        self.src2 = pts_src[1]
        self.src3 = pts_src[2]
        self.src4 = pts_src[3]

        self.dest1 = pts_dst[0]
        self.dest2 = pts_dst[1]
        self.dest3 = pts_dst[2]
        self.dest4 = pts_dst[3]

        self.calculate_homography()

    def calculate_homography(self):
        xs_1 = self.src1[0]
        ys_1 = self.src1[1]

        xs_2 = self.src2[0]
        ys_2 = self.src2[1]

        xs_3 = self.src3[0]
        ys_3 = self.src3[1]

        xs_4 = self.src4[0]
        ys_4 = self.src4[1]

        xd_1 = self.dest1[0]
        yd_1 = self.dest1[1]

        xd_2 = self.dest2[0]
        yd_2 = self.dest2[1]

        xd_3 = self.dest3[0]
        yd_3 = self.dest3[1]

        xd_4 = self.dest4[0]
        yd_4 = self.dest4[1]

        a = np.array([[-xs_1,-ys_1, -1, 0, 0, 0, xs_1*xd_1, ys_1*xd_1, xd_1],
                      [0, 0, 0, -xs_1, -ys_1, -1, xs_1*yd_1, ys_1*yd_1, yd_1],
                      [-xs_2,-ys_2, -1, 0, 0, 0, xs_2*xd_2, ys_2*xd_2, xd_2],
                      [0, 0, 0, -xs_2, -ys_2, -1, xs_2*yd_2, ys_2*yd_2, yd_2],
                      [-xs_3,-ys_3, -1, 0, 0, 0, xs_3*xd_3, ys_3*xd_3, xd_3],
                      [0, 0, 0, -xs_3, -ys_3, -1, xs_3*yd_3, ys_3*yd_3, yd_3],
                      [-xs_4,-ys_4, -1, 0, 0, 0, xs_4*xd_4, ys_4*xd_4, xd_4],
                      [0, 0, 0, -xs_4, -ys_4, -1, xs_4*yd_4, ys_4*yd_4, yd_4]])

        _, _, vh = np.linalg.svd(a, full_matrices=True)

        print("vh: ", vh)

        self.h = vh[:, vh.shape[1]-1]
        print("h:", self.h)
        self.h = np.reshape(self.h, (3,3))

    def get_homography_matrix(self):
        return self.h

    def map(self):
        pass

if __name__ == "__main__":
    import cv2

    pts_src = np.array([[141, 131], [480, 159], [493, 630], [64, 601]], np.float32)
    pts_dst = np.array([[318, 256], [534, 372], [316, 670], [73, 473]], np.float32)

    h = cv2.getPerspectiveTransform(pts_src, pts_dst)
    print(h)

    hh, status = cv2.findHomography(pts_src, pts_dst)
    print(hh)

    homographer = Homographer(pts_src, pts_dst)
    print(homographer.get_homography_matrix())