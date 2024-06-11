# cowlar-hyper-growth-1


# Concept Notes:

## Principal component Analysis
It is a dimensionality reduction technique to reduce n number of factors to a smaller m number of factors in such a way that the new factors are end-correlated and ranked from most important to least important.
## Fourier Transform
Fourier Transform is a mathematical technique used to split a signal made up of multiple pure frequencies and finding our what those original frequencies are.

## Computer Vision Annotation formats

YOLO Darknet
```txt
class_id center_c center_y width height
```

VoTT Json (MS VoTT tool)
```json
{ 
	"asset": { 
		"format": "jpg", 
		"id": "0a2ac9053d4d842653d3ff9f988421a6", 
		"name": "img0001.jpg", 
		"path": "file:D:/HardHats/img0001.jpg", 
		"size": { 
			"width": 612, 
			"height": 408 
		}, 
		"state": 2, 
		"type": 1 
	}, 
	"regions": [ 
		{ 
			"id": "XEhNEKjZT", 
			"type": "RECTANGLE", 
			"tags": [ 
				"helmet" 
			], 
			"boundingBox": { 
				"height": 204, 
				"width": 505.5652173913043, 
				"left": 32.06688963210702, 
				"top": 143.9598662207358 
			}, 
			"points": [ 
				{ 
				"x": 32.06688963210702,
				"y": 143.9598662207358 
				}, 
				{ 
				"x": 537.6321070234113, 
				"y": 143.9598662207358 
				}, 
				{ 
				"x": 537.6321070234113, 
				"y": 347.95986622073576 
				}, 
				{ 
				"x": 32.06688963210702, 
				"y": 347.95986622073576 
				} 
			] 
		} 
	], 
	"version": "2.1.0" 
}
```
Tensorflow Object Detection CSV
```txt
filename,width,height,class,xmin,ymin,xmax,ymax
```
COCO Json, Pascal VOC XML, 

## Can Gunicorn run async workers?
Yes, using gevent worker type

## Object detection metrics
IOU
Precision and Recall
Average Precision
Mean Average Precision (mAP) (AP but for multiclass) [link](https://kili-technology.com/data-labeling/machine-learning/mean-average-precision-map-a-complete-guide) [categories](https://www.researchgate.net/figure/Mean-average-precision-mAP-graphs-for-the-categories-mAP-05-represents-the-mAP-value_fig6_364969172#:~:text=for%20the%20categories.-,mAP_0.,0.85%2C%200.9%2C%200.95))

## KNN best value of K using elbow method

Visual technique to identify the optimal K value by plotting error with respect to K. k after which error doesn't decrease meaningfully should be selected. Optimal K prevents underfitting and overfitting.

## Decision tree Pruning
- During training, remove branches of the tree with low predictive power to avoid overfitting.
- Post pruning where we use max-depth and min-samples-split to drop branches. this reduces complexity and avoids overfitting.
- Pre Pruning is just early stopping for decision trees


# Internet Speed checker using Python
- The actual script is saved in [python file](auto-internet-speed-checker\script.py)
- This code uses speedtest-cli library to check internet speed. 
- The [visualzation code](auto-internet-speed-checker\visualize.py) is used to plot the data. The output looks like this:
![Internet Speed](auto-internet-speed-checker\internet_speed_plot.jpg)

## To run as a scheduled container, use the docker compose file
```bash
docker-compose up -d
```

## To run as a scheduled service on linux, us the following systemd commands to create a service
```bash
chmod +x auto-internet-speed-checker/systemd_scheduler.sh
cp auto-internet-speed-checker/auto-internet-speed-checker.service /etc/systemd/system/
cp auto-internet-speed-checker/systemd_scheduler.sh /usr/local/bin/
sudo systemctl daemon-reload
sudo systemctl start auto-internet-speed-checker
sudo systemctl enable auto-internet-speed-checker
```
