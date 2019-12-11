# Video/Image Converter
A python implementation of encoding images to video and decoding video to images.

## Dependencies:
1. opencv-python (with numpy) 
2. tqdm (optional, for progress visualization)

Install with command:
```
pip3 install opencv-python
pip3 install tqdm
```

## Video to Image:
```
python3 vid2img.py [video_path] -to [output_image_format] -o [output_image_path_name] -v
```
1. output image format: `'.jpg'`(default), `'.bmp'`, ... (all image format supported by cv2.imwrite)
2. output path + name : `img/img`(default).
3. Use `-v` to show the progress bar. 

## Image to Video:
```
python3 img2vid.py [image_path] -ti [image_format] -o [output_video_path_name] -to [output_video_format] -f [frame_rate] -v
```
1. image format: `'.jpg'`(default), `'.bmp'`, ... (all image format supported by cv2.imread)
2. output video path + name : `out`(default).
3. output video fomat: `.mp4`(default), `'.avi'` 
4. frame rate: `30`(default)
5. Use `-v` to show the progress bar. 