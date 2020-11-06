//히스토그램 평활화

#include <stdio.h>
#include <windows.h>

#pragma warning(disable:4996)

int main() {

	FILE* fp;
	unsigned char* f = NULL;
	unsigned char* fout = NULL;
	unsigned int hist[256] = { 0 };
	float hist_E[256] = { 0.0 };
	float c[256] = { 0.0 };

	f = (unsigned char*)malloc(139876);
	fout = (unsigned char*)malloc(139876);

	fp = fopen("lenna.raw", "rb");
	fread(f, 1, 139876, fp);
	fclose(fp);

	for (int i = 0; i < 139876; i++) {
		hist[f[i]]++;
	} // 영상 히스토그램 생성

	for (int i = 0; i < 256; i++) {

		hist_E[i] = (float)hist[i] / 139876;
	} // 영상 히스토그램 정규화

	c[0] = hist_E[0];
	for (int i = 1; i < 256; i++) {
		c[i] = c[i - 1] + hist_E[i];
	} //영상 누적 히스토그램


	for (int i = 0; i < 139876; i++) {
		fout[i] = c[f[i]] * 255;
	} //평활화

	fp = fopen("lenna_hist.raw", "wb");
	fwrite(fout, 1, 139876, fp);
	fclose(fp);



	free(f);
	free(fout);


	return 0;
}
