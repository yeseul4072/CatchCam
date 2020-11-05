package com.ssafy.catchcam.service;

import java.util.List;

import com.ssafy.catchcam.model.RentalRequest;
import com.ssafy.catchcam.model.RentalResponse;
import com.ssafy.catchcam.model.StoreResponse;

public interface RentalService {

	//대여 목록 조회
	public List<RentalResponse> getRentalList() throws Exception;
	
	//대여하기
	public void insertRental(RentalRequest rental) throws Exception;

	//지점 목록 조회
	public List<StoreResponse> getStoreList() throws Exception;
}
