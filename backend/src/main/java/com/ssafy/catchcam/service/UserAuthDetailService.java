package com.ssafy.catchcam.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

//import com.ssafy.devit.model.user.UserAuthDetails;
//import com.ssafy.devit.repository.UserRepository;

@Service
public class UserAuthDetailService implements UserDetailsService{
	/*@Autowired
	private UserRepository userRepository;*/

	// UserDetailsService Eamil로 유저 검색(Security 관련)
	@Override
	public UserDetails loadUserByUsername(String userId) throws UsernameNotFoundException {
//		UserAuthDetails userDetails = null;
//		try {
//			userDetails =  userRepository.findUserByUserId(Long.parseLong(userId));
//		} catch (Exception e) {
//			throw new UsernameNotFoundException("사용자를 찾을 수 없습니다");
//		}
//		return userDetails;
		return null;
	}
	/*
	public int checkValidEmailOrNickname(String email, String nickname) throws Exception{
		if(email.equals("") || nickname.equals("")) {
			throw new Exception("이메일 또는 닉네임은 비어있을 수 없습니다");
		}
		return userRepository.checkValidEmailOrNickname(email, nickname);
	}
	
	// 회원 가입
	public void signUp(UserAuthDetails user) throws Exception {
		userRepository.insertUser(user);
	}
	
	// 이메일로 사용자 검색 부터 시작
	public UserAuthDetails getUserByEmail(String email) throws Exception{
		if(email.equals("")) {
			throw new Exception("이메일은 비어있을 수 없습니다");
		}
		return userRepository.findUserByEmail(email);
	}

	// 권한 가져오기
	public List<String> getRoles(long userId) throws Exception {
		if(userId < 1) {
			throw new Exception("잘못된 접근 입니다");
		}
		return userRepository.findRoles(userId);
	}
	
	// 이메일로 사용자 활성화 여부 가져오기
	public String getUserActiveByEmail(String email) throws Exception{
		if(email.equals("")) {
			throw new Exception("이메일은 비어있을 수 없습니다");
		}
		return userRepository.findUserActiveByEmail(email);
	}*/
}
