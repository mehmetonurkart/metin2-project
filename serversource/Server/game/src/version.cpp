#include <stdio.h>

void WriteVersion()
{
#ifndef __WIN32__
	FILE* fp = fopen("VERSION.txt", "w");

	if (fp)
	{
		fprintf(fp, "game svn revision: %s\n", __SVN_VERSION__);
		fclose(fp);
	}
#endif
}

