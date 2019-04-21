import numpy as np
import cv2

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
        
        print(self.src0, self.src1, self.src2, self.src3)

    def set_destination_points(self, pts_dst):
        self.dest0 = pts_dst[0]
        self.dest1 = pts_dst[1]
        self.dest2 = pts_dst[2]
        self.dest3 = pts_dst[3]
        
        print(self.dest0, self.dest1, self.dest2, self.dest3)

    def calculate_homography(self):
        self.H, status = cv2.findHomography(np.array([self.src0, self.src1, self.src2, self.src3]), np.array([self.dest0, self.dest1, self.dest2, self.dest3]))

    def transform_coordinates(self, pt_src):
        if self.H is not None:
            print(self.H.shape)
            pt_dest = np.matmul(pt_src, self.H)
            
            return pt_dest
        else:
            return pt_src
        
    def reset_homography(self):
        self.src0 = None
        self.src1 = None
        self.src2 = None
        self.src3 = None

        self.dest0 = None
        self.dest1 = None
        self.dest2 = None
        self.dest3 = None

        self.H = None

if __name__ == "__main__":
    import cv2

    pts_src = np.array([[88, 210], [465, 72], [886, 383], [460, 604]], np.float32)
    pts_dst = np.array([[0, 0], [300, 0], [300, 400], [0, 400]], np.float32)

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
    cv2.imshow("orig", orig_src)
    # area = cv2.contourArea()

    dst = np.zeros((400, 400))
    dst = cv2.warpPerspective(orig_src, homographer.H, dst.shape)

    print(dst)

    cv2.imshow("test", dst)
    cv2.waitKey()