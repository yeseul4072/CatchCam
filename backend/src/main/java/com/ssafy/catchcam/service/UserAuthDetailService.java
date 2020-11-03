package com.ssafy.catchcam.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.ssafy.catchcam.model.UserAuthDetails;
import com.ssafy.catchcam.repository.UserRepository;

@Service
public class UserAuthDetailService implements UserDetailsService{
	@Autowired
	private UserRepository userRepository;

	// UserDetailsService Email로 유저 검색(Security 관련)
	@Override
	public UserDetails loadUserByUsername(String userId) throws UsernameNotFoundException {
		UserAuthDetails userDetails = null;
		try {
			userDetails =  userRepository.findUserByUserId(Long.parseLong(userId));
		} catch (Exception e) {
			throw new UsernameNotFoundException("사용자를 찾을 수 없습니다");
		}
		return userDetails;
	}
	
	public int checkValidEmail(String email) throws Exception{
		if(email.equals("")) {
			throw new Exception("이메일은 비어있을 수 없습니다");
		}
		return userRepository.checkValidEmail(email);
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

}
