---
title: Thresholding multi-channel images like CMYK using OpenCV
generated: true
---

<div markdown="1" class="ans">
```python
# Thresholding C and K values
binaryImage = cv.inRange(
    inputImageCMYK,
    (128,   0,   0,   0),
    (255, 255, 255, 196))
```
</div>

**Remarks:**

You can then display the thresholded images:
```python
plt.imshow(binaryImage, cmap='gray')
```
