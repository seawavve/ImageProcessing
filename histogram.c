#include <stdio.h>
#include <windows.h>

#pragma warning(disable:4996)

int main() {

	FILE* fp;
	unsigned char* f = NULL;
	unsigned int hist[256] = { 0 };

	f = (unsigned char*)malloc(139876); 
	fp = fopen("lenna.raw", "rb");
	fread(f, 1, 139876, fp);

	for (int i = 0; i < 139876; i++) {	//히스토그램 만들기
		hist[f[i]]++;
	}

	for (int i = 0; i < 256; i++)printf("%3d\n", hist[i]); //가시화

	fclose(fp);
	free(f);


	return 0;
}
