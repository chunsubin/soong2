% clear;
% clear all;
% 
% droneObj = ryze();
% 
% cameraObj = camera(droneObj);
% preview(cameraObj);
% while 1
%     [frame,ts] = snapshot(cameraObj);
%     
%     hsv = rgb2hsv(frame);
%     h = hsv(:,:,1);
%     h = h(360, 480)
%     s = hsv(:,:,2);
%     s = s(360, 480)
% end

red = bwareaopen(detect_red, 700);
imshow(red);

% nnz(detect_red)