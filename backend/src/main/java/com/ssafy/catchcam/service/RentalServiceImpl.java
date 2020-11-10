package com.ssafy.catchcam.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;

import com.ssafy.catchcam.model.ItemResponse;
import com.ssafy.catchcam.model.RentalRequest;
import com.ssafy.catchcam.model.RentalResponse;
import com.ssafy.catchcam.model.ReviewListResponse;
import com.ssafy.catchcam.model.ReviewRequest;
import com.ssafy.catchcam.model.StoreResponse;
import com.ssafy.catchcam.model.UserAuthDetails;
import com.ssafy.catchcam.repository.RentalRepository;

@Service
public class RentalServiceImpl implements RentalService {
	
	@Autowired
	RentalRepository rentalRepository;
	
	@Override
	public List<RentalResponse> getRentalList() throws Exception{
		UserAuthDetails user = (UserAuthDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		return rentalRepository.getRentalList(user.getUserId());
	}
	
	@Override
	public void insertRental(RentalRequest rental) throws Exception{
		rentalRepository.insertRental(rental);
	}

	@Override
	public List<StoreResponse> getStoreList() throws Exception{
		return rentalRepository.getStoreList();
	}
	
	@Override
	public ItemResponse getItemInfo(long itemId) throws Exception{
		return rentalRepository.getItemInfo(itemId);
	}

	@Override
	public ReviewListResponse getReviewList(long itemId, long userId) throws Exception{
		ReviewListResponse reviewList = rentalRepository.getItemReview(itemId, userId);
		if(reviewList != null) {
			reviewList.setReviews(rentalRepository.getReviewList(itemId, userId));
		}
		return reviewList;
	}
	
	@Override
	public void insertReview(ReviewRequest rental) throws Exception{
		UserAuthDetails user = (UserAuthDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();

		//유저와 대여자가 같은지 확인
		if("N".equals(rentalRepository.checkRentalUser(rental.getRentalId(), user.getUserId()))) {
			throw new Exception("리뷰 작성 권한이 없습니다.");
		}
		
		rentalRepository.insertReview(rental, user.getUserId());
	}
	
	@Override
	public void updateReview(ReviewRequest rental) throws Exception{
		UserAuthDetails user = (UserAuthDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();

		//유저와 리뷰등록자가 같은지 확인
		if("N".equals(rentalRepository.checkReviewUser(rental.getReviewId(), user.getUserId()))) {
			throw new Exception("리뷰 수정 권한이 없습니다.");
		}
		rentalRepository.updateReview(rental);
	}
	
	@Override
	public void deleteReview(long reviewId) throws Exception{
		
		if(reviewId < 1) {
			throw new Exception("유효하지 않은 리뷰입니다.");
		}

		UserAuthDetails user = (UserAuthDetails) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
		
		//유저와 리뷰등록자가 같은지 확인
		if("N".equals(rentalRepository.checkReviewUser(reviewId, user.getUserId()))) {
			throw new Exception("리뷰 삭제 권한이 없습니다.");
		}
		
		//존재여부 확인하기
		rentalRepository.deleteReview(reviewId);
	}
	
}