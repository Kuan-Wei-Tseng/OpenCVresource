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

## Video to Image
```
python3 vid2img.py [video_path] -to [output image format] -o [output image path + name] 
```
1. output image format: `'.jpg'`(default), `'.bmp'`, ... (all image format supported by cv2.imwrite)
2. output path + name : `img/img`(default).
3. Use `-v` to show the progress bar. 
