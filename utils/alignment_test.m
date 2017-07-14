function error_per_image = alignment_test()
    annotation='/home/zhangbin/Alignment/dataset/ibug/';
    detection='/home/zhangbin/Alignment/dataset/ibug-/';
    [ground_truth_all, detected_points_all] = get_points(annotation, detection);
    error_per_image = compute_error(ground_truth_all, detected_points_all);
    f = fopen('test.txt', 'w');
    len = size(error_per_image, 1);
    for i=1:len
        fprintf(f,'%f\n', error_per_image(i));
    end
    fclose(f);
end

function [ground_truth_all, detected_points_all] = get_points(annotation, detection)
    fileExt = '*.pts';
    files = dir(fullfile(annotation,fileExt));
    %files = sort(files, 1);
    len = size(files, 1);
    ground_truth_all = zeros(68, 68, len);
    A=zeros(68,68);
    for i=1:len  
        fileName = strcat(annotation,files(i,1).name);
        in = fopen(fileName);
        fgetl(in);fgetl(in);fgetl(in);
        for j=1:68
            line = fgetl(in);
            S = regexp(line, ' ', 'split');
            A(j,1)=str2num(S{1});
            A(j,2)=str2num(S{2});
        end
        ground_truth_all(:,:,i)=A; 
        fclose(in);
    end
    
    files = dir(fullfile(detection,fileExt));
    %files = sort(files);
    len = size(files, 1);
    detected_points_all = zeros(68,68,len);
    B=zeros(68, 68);
    for i=1:len  
        fileName = strcat(detection,files(i,1).name);
        in = fopen(fileName);
        fgetl(in);fgetl(in);fgetl(in);    
        for j=1:68
            line = fgetl(in);
            S = regexp(line, ' ', 'split');
            B(j,1)=str2num(S{1}) + 0.5;
            B(j,2)=str2num(S{2}) + 1;
            
        end
        detected_points_all(:,:,i)=B; 
        fclose(in);
    end
end

function [ error_per_image ] = compute_error( ground_truth_all, detected_points_all )
%compute_error
%   compute the average point-to-point Euclidean error normalized by the
%   inter-ocular distance (measured as the Euclidean distance between the
%   outer corners of the eyes)
%
%   Inputs:
%          grounth_truth_all, size: num_of_points x 2 x num_of_images
%          detected_points_all, size: num_of_points x 2 x num_of_images
%   Output:
%          error_per_image, size: num_of_images x 1
    num_of_images = size(ground_truth_all,3);
    num_of_points = size(ground_truth_all,1);
    error_per_image = zeros(num_of_images,1);
    for i =1:num_of_images
        detected_points      = detected_points_all(:,:,i);
        ground_truth_points  = ground_truth_all(:,:,i);
        if num_of_points == 68
            interocular_distance = norm(ground_truth_points(37,:)-ground_truth_points(46,:));
        elseif num_of_points == 51
            interocular_distance = norm(ground_truth_points(20,:)-ground_truth_points(29,:));
        end

        sum=0;
        for j=1:num_of_points
            sum = sum+norm(detected_points(j,:)-ground_truth_points(j,:));
        end
        error_per_image(i) = sum/(num_of_points*interocular_distance);
    end
end


