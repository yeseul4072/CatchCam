package com.ssafy.catchcam.model;

import java.util.Date;

public class RentalResponse {
	private long rentalId;
	private long itemId;
	private long userId;
	private long storeId;
	private Date rentDate;
	private Date returnDate;
	private Date actReturnDate;

	public RentalResponse() {

	}

	public long getRentalId() {
		return rentalId;
	}

	public void setRentalId(long rentalId) {
		this.rentalId = rentalId;
	}

	public long getItemId() {
		return itemId;
	}

	public void setItemId(long itemId) {
		this.itemId = itemId;
	}

	public long getUserId() {
		return userId;
	}

	public void setUserId(long userId) {
		this.userId = userId;
	}

	public long getStoreId() {
		return storeId;
	}

	public void setStoreId(long storeId) {
		this.storeId = storeId;
	}

	public Date getRentDate() {
		return rentDate;
	}

	public void setRentDate(Date rentDate) {
		this.rentDate = rentDate;
	}

	public Date getReturnDate() {
		return returnDate;
	}

	public void setReturnDate(Date returnDate) {
		this.returnDate = returnDate;
	}

	public Date getActReturnDate() {
		return actReturnDate;
	}

	public void setActReturnDate(Date actReturnDate) {
		this.actReturnDate = actReturnDate;
	}
	
	

}
