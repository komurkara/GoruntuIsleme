import numpy as np
import argparse
import cv2

public void medianFiltresi ()
{
    Color OkunanRenk;
    Bitmap GirisResmi, CikisResmi;
    GirisResmi = new Bitmap(vesikalik.jpg);
    int ResimGenisligi = GirisResmi.Width;
    int ResimYuksekligi = GirisResmi.Height;
    CikisResmi = new Bitmap(ResimGenisligi, ResimYuksekligi);
    int SablonBoyutu = 3; //şablon boyutu 3 den büyük tek rakam olmalıdır (3,5,7 gibi).
    int ElemanSayisi = SablonBoyutu * SablonBoyutu;
    int[] R = new int[ElemanSayisi];
    int[] G = new int[ElemanSayisi];
    int[] B = new int[ElemanSayisi];
    int[] Gri = new int[ElemanSayisi];
    int x, y, i, j;
    for (x = (SablonBoyutu - 1) / 2; x < ResimGenisligi - (SablonBoyutu - 1) / 2; x++)
    {
        for (y = (SablonBoyutu - 1) / 2; y < ResimYuksekligi - (SablonBoyutu - 1) / 2; y++)
        {
            //Şablon bölgesi (çekirdek matris) içindeki pikselleri tarıyor.
            int k = 0;
            for (i = -((SablonBoyutu - 1) / 2); i <= (SablonBoyutu - 1) / 2; i++)
            {
                for (j = -((SablonBoyutu - 1) / 2); j <= (SablonBoyutu - 1) / 2; j++)
                {
                    OkunanRenk = GirisResmi.GetPixel(x + i, y + j);
                    R[k] = OkunanRenk.R;
                    G[k] = OkunanRenk.G;
                    B[k] = OkunanRenk.B;
                    Gri[k] = Convert.ToInt16(R[k] * 0.299 + G[k] * 0.587 + B[k] * 0.114); //Gri ton formülü
                    k++;
                }
            }
            //Gri tona göre sıralama yapıyor. Aynı anda üç rengide değiştiriyor.
            int GeciciSayi = 0;
            for (i = 0; i < ElemanSayisi; i++)
            {
                for (j = i + 1; j < ElemanSayisi; j++)
                {
                if (Gri[j] < Gri[i])
                {
                    GeciciSayi = Gri[i];
                    Gri[i] = Gri[j];
                    Gri[j] = GeciciSayi;
                    GeciciSayi = R[i];
                    R[i] = R[j];
                    R[j] = GeciciSayi;
                    GeciciSayi = G[i];
                    G[i] = G[j];
                    G[j] = GeciciSayi;
                    GeciciSayi = B[i];
                    B[i] = B[j];
                }
            }
        }
        //Sıralama sonrası ortadaki değeri çıkış resminin piksel değeri olarak atıyor.
        CikisResmi.SetPixel(x, y, Color.FromArgb(R[(ElemanSayisi - 1) / 2], G[(ElemanSayisi - 1) /2], B[(ElemanSayisi - 1) / 2]));
    }
 }
 pictureBox2.Image = CikisResmi; }