package com.ssafy.catchcam.config.security;

import java.io.IOException;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.GenericFilterBean;

public class JwtAuthenticationFilter extends GenericFilterBean {

	@Autowired
	private JwtTokenProvider jwtTokenProvider;

	public JwtAuthenticationFilter(JwtTokenProvider jwtTokenProvider) {
		this.jwtTokenProvider = jwtTokenProvider;
	}

	// Requestλ‘? ?€?΄?€? Jwt Token? ? ?¨?±? κ²?μ¦?(jwtTokenProvider.validateToken)?? filterλ₯?
	// filterChain? ?±λ‘ν©??€.
	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain filterChain)
			throws IOException, ServletException {
		// ?€??? JWTλ₯? λ°μ?΄
		String token = jwtTokenProvider.resolveToken((HttpServletRequest) request);
		// ? ?¨? ? ?°?Έμ§? ??Έ
		if (token != null && jwtTokenProvider.validateToken(token)) {
			// ? ?°?΄ ? ?¨?λ©? ? ?°?Όλ‘? λΆ??° ? ?? ? λ³? λ°μ?΄
			Authentication authentication = jwtTokenProvider.getAuthentication(token);
			
			SecurityContextHolder.getContext().setAuthentication(authentication);
		}
		filterChain.doFilter(request, response);
	}
}
