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

    def set_source_points(self, src_func):
        pts_src = src_func()
        
        if type(pts_src[0]) != np.ndarray:
            pts_src = self.qpoints_to_array(pts_src)
        print(pts_src)    
        
        self.src0 = pts_src[0]
        self.src1 = pts_src[1]
        self.src2 = pts_src[2]
        self.src3 = pts_src[3]

    def set_destination_points(self, dst_func):
        pts_dst = dst_func()
        
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
            try:
                pt = np.array([[[pt_src[0], pt_src[1]]]], dtype=np.float32)
                print(pt, pt.shape)
                result = cv2.perspectiveTransform(pt, self.H)
                print(result)
                pt_dest = [result[0][0][0], result[0][0][1]]
            
                return pt_dest
            except Exception as e:
                print(e)
                raise ValueError("invalid point")
        else:
            return [pt_src[0], pt_src[1]]
        
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