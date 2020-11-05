package com.ssafy.catchcam.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.ssafy.catchcam.model.RentalRequest;
import com.ssafy.catchcam.model.RentalResponse;
import com.ssafy.catchcam.model.StoreResponse;
import com.ssafy.catchcam.repository.RentalRepository;

@Service
public class RentalServiceImpl implements RentalService {
	
	@Autowired
	RentalRepository rentalRepository;
	
	@Override
	public List<RentalResponse> getRentalList() throws Exception{
		return rentalRepository.getRentalList();
	}
	
	@Override
	public void insertRental(RentalRequest rental) throws Exception{
		rentalRepository.insertRental(rental);
	}

	@Override
	public List<StoreResponse> getStoreList() throws Exception{
		return rentalRepository.getStoreList();
	}
}