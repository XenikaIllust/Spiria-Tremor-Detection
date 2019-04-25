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
        
    def qpoints_to_array(self, qpoints):
        points = []
        for qpoint in qpoints:
            point = [qpoint.x(), qpoint.y()]
            points.append(point)
        return points

    def set_source_points(self, pts_src):
        if type(pts_src[0]) != np.ndarray:
            pts_src = self.qpoints_to_array(pts_src)
        self.src0 = pts_src[0]
        self.src1 = pts_src[1]
        self.src2 = pts_src[2]
        self.src3 = pts_src[3]

    def set_destination_points(self, pts_dst):
        if type(pts_dst[0]) != np.ndarray:
            pts_dst = self.qpoints_to_array(pts_dst)
        self.dest0 = pts_dst[0]
        self.dest1 = pts_dst[1]
        self.dest2 = pts_dst[2]
        self.dest3 = pts_dst[3]

    def calculate_homography(self):
        print([self.src0, self.src1, self.src2, self.src3], [self.dest0, self.dest1, self.dest2, self.dest3])
        self.H, status = cv2.findHomography(np.array([self.src0, self.src1, self.src2, self.src3]), np.array([self.dest0, self.dest1, self.dest2, self.dest3]))

    def transform_coordinates(self, pt_src):
        if self.H is not None:
            result = np.matmul(pt_src, self.H)
            # pt_dest = [result[0][0]/abs(result[0][2]), result[0][1]/abs(result[0][2])]
            pt_dest = [abs(result[0][0]), abs(result[0][1])]
            
            return pt_dest
        else:
            return [pt_src[0][0], pt_src[0][1]]
        
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
    
    # pts_src = np.array([[0, 255], [1023, 255], [1023, 1023], [0, 1023]], np.float32)
    # pts_dst = np.array([[0, 0], [300, 0], [300, 300], [0, 300]], np.float32)

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

    dst = np.zeros((300, 400))
    dst = cv2.warpPerspective(orig_src, homographer.H, dst.shape)

    print(dst)

    cv2.imshow("test", dst)
    cv2.waitKey()