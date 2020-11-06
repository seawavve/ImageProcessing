#include <stdio.h>
#include <windows.h>
#define WIDTH 374
#define HEIGHT 374
#define N 3
#define M 3
#pragma warning(disable:4996)


int main() {

	FILE *fp;
	unsigned char *InImg = NULL;
	unsigned char *OutImg = NULL;


	//수직에지
	float mask[N][M] = { {1.0, 0.0, -1.0},
			{1.0, 0.0, -1.0},
			{1.0, 0.0, -1.0} };

	InImg = (unsigned char*)malloc(WIDTH*HEIGHT);
	OutImg = (unsigned char*)malloc(WIDTH*HEIGHT);

	memset(InImg, 0, WIDTH*HEIGHT);
	memset(OutImg, 0, WIDTH*HEIGHT);
	fp = fopen("lenna.raw", "rb");
	fread(InImg, 1, WIDTH*HEIGHT, fp);
	fclose(fp);

	//OutImg[i] = InImg[i] * mask[N][M]
	for (int i = 0; i < WIDTH*HEIGHT; i++) {
		int hh = i / WIDTH;
		int ww = i % WIDTH;
		float ConImg = 0.0;

		if (hh >= N / 2 && hh < HEIGHT - N/2 && ww >= M/2 && ww < WIDTH - M/2) {
			for (int ii = -N/2; ii < N/2+1; ii++) {
				for (int jj = -M/2; jj < M/2+1; jj++) {
					ConImg += (float)InImg[(hh+ii)*WIDTH+ww+jj] * mask[ii+N/2][jj+M/2];
				}
			}
		}
		if (ConImg > 255.0)ConImg = 255.0;
		else if (ConImg < 0.0)ConImg = 0.0;

		OutImg[i] = (unsigned char)ConImg;
	}

	fp = fopen("lenna_mask.raw", "wb");
	fwrite(OutImg, 1, WIDTH*HEIGHT, fp);
	fclose(fp);

	return 0;
}
