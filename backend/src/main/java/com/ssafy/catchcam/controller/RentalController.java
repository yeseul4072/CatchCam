package com.ssafy.catchcam.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.ssafy.catchcam.model.CommonResponse;
import com.ssafy.catchcam.model.RentalRequest;
import com.ssafy.catchcam.service.RentalService;

import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;

@RestController
public class RentalController {

	Logger log = LoggerFactory.getLogger(this.getClass());


	@Autowired
	RentalService rentalService;
	
	@ApiImplicitParams({
		@ApiImplicitParam(name = "X-AUTH-TOKEN", value = "로그인 성공 후 access_token", required = true, dataType = "String", paramType = "header") })
	@PostMapping("/rental")
	@ApiOperation(value = "대여 등록")
	public ResponseEntity<CommonResponse> insertRental(@RequestBody RentalRequest request) throws Exception{
		log.info(">> Load : insertRental <<");
		ResponseEntity<CommonResponse> response = null;
		final CommonResponse result = new CommonResponse();
		try {
			rentalService.insertRental(request);
			result.result = "대여 신청이 완료되었습니다.";
			result.msg = "success";
			response = new ResponseEntity<CommonResponse>(result, HttpStatus.OK);
		} catch (Exception e) {
			log.info(">> Error : insertRental <<");
			log.info(e.getMessage().toString());
			result.msg = "fail";
			result.result = e.getMessage().toString();
			response = new ResponseEntity<CommonResponse>(result, HttpStatus.OK);
		}
		return response;
	}

	@ApiImplicitParams({
			@ApiImplicitParam(name = "X-AUTH-TOKEN", value = "로그인 성공 후 access_token", required = true, dataType = "String", paramType = "header") })
	@GetMapping("/rentals")
	@ApiOperation(value = "모든 대여 목록 조회")
	public ResponseEntity<CommonResponse> getRentalList() {
		log.info(">> Load : getRentalList <<");
		ResponseEntity<CommonResponse> response = null;
		final CommonResponse result = new CommonResponse();

		try {
			result.result = rentalService.getRentalList();
			result.msg = "success";
			response = new ResponseEntity<CommonResponse>(result, HttpStatus.OK);
		} catch (Exception e) {
			result.msg = "fail";
			response = new ResponseEntity<CommonResponse>(result, HttpStatus.BAD_REQUEST);
			log.info(">> Error : getRentalList <<");
			log.info(e.getMessage().toString());
		}
		return response;
	}

	@ApiImplicitParams({
			@ApiImplicitParam(name = "X-AUTH-TOKEN", value = "로그인 성공 후 access_token", required = true, dataType = "String", paramType = "header") })
	@GetMapping("/stores")
	@ApiOperation(value = "모든 지점 목록 조회")
	public ResponseEntity<CommonResponse> getStoreList() {
		log.info(">> Load : getStoreList <<");
		ResponseEntity<CommonResponse> response = null;
		final CommonResponse result = new CommonResponse();

		try {
			result.result = rentalService.getStoreList();
			result.msg = "success";
			response = new ResponseEntity<CommonResponse>(result, HttpStatus.OK);
		} catch (Exception e) {
			result.msg = "fail";
			response = new ResponseEntity<CommonResponse>(result, HttpStatus.BAD_REQUEST);
			log.info(">> Error : getStoreList <<");
			log.info(e.getMessage().toString());
		}
		return response;
	}
}
