import { Camera } from '@capacitor/camera';

export async function captureEvidence() {
  return Camera.getPhoto({ quality: 80 });
}
