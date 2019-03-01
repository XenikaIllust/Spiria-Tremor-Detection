import numpy as np

class Homographer():
    def __init__(self):
        self.src0 = None
        self.src1 = None
        self.src2 = None
        self.src3 = None

        self.dest0 = None
        self.dest1 = None
        self.dest2 = None
        self.dest3 = None

        self.H = None

    def set_source_points(self, pts_src):
        self.src0 = pts_src[0]
        self.src1 = pts_src[1]
        self.src2 = pts_src[2]
        self.src3 = pts_src[3]

    def set_destination_points(self, pts_dst):
        self.dest0 = pts_dst[0]
        self.dest1 = pts_dst[1]
        self.dest2 = pts_dst[2]
        self.dest3 = pts_dst[3]

    def calculate_homography(self):
        """
        xs_1 = self.src0[0]
        ys_1 = self.src0[1]

        xs_2 = self.src1[0]
        ys_2 = self.src1[1]

        xs_3 = self.src2[0]
        ys_3 = self.src2[1]

        xs_4 = self.src3[0]
        ys_4 = self.src3[1]

        xd_1 = self.dest0[0]
        yd_1 = self.dest0[1]

        xd_2 = self.dest1[0]
        yd_2 = self.dest1[1]

        xd_3 = self.dest2[0]
        yd_3 = self.dest2[1]

        xd_4 = self.dest3[0]
        yd_4 = self.dest3[1]

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

        self.H = vh[:, vh.shape[1]-1]
        print("h:", self.h)
        self.H = np.reshape(self.H, (3,3))
        """

        self.H, status = cv2.findHomography(np.array([self.src0, self.src1, self.src2, self.src3]), np.array([self.dest0, self.dest1, self.dest2, self.dest3]))


    def transform_coordinates(self, pt_src):
        pt_dest = np.matmul(pt_src, self.H)
        return pt_dest

if __name__ == "__main__":
    import cv2

    pts_src = np.array([[60, 139], [312, 48], [587, 254], [304, 398]], np.float32)
    pts_dst = np.array([[0, 0], [200, 0], [200, 400], [0, 400]], np.float32)

    # h = cv2.getPerspectiveTransform(pts_src, pts_dst)
    # print(h)
    #
    # hh, status = cv2.findHomography(pts_src, pts_dst)
    # print(hh)

    homographer = Homographer()
    homographer.set_source_points(pts_src)
    homographer.set_destination_points(pts_dst)
    homographer.calculate_homography()
    print(homographer.H)
    print(homographer.transform_coordinates(np.array([60, 139, 1])))

    orig_src = cv2.imread("../assets/images/test_homography.jpg")
    # area = cv2.contourArea()

    dst = np.zeros((400, 400))
    dst = cv2.warpPerspective(orig_src, homographer.H, dst.shape)

    print(dst)

    cv2.imshow("test", dst)
    cv2.waitKey()