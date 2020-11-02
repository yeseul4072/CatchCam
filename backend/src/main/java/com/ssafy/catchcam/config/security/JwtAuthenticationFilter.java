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

	// RequestÎ°? ?ì§?ñ¥?ò§?äî Jwt Token?ùò ?ú†?ö®?Ñ±?ùÑ Í≤?Ï¶?(jwtTokenProvider.validateToken)?ïò?äî filterÎ•?
	// filterChain?óê ?ì±Î°ùÌï©?ãà?ã§.
	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain filterChain)
			throws IOException, ServletException {
		// ?ó§?çî?óê?Ñú JWTÎ•? Î∞õÏïÑ?ò¥
		String token = jwtTokenProvider.resolveToken((HttpServletRequest) request);
		// ?ú†?ö®?ïú ?Ü†?Å∞?ù∏Ïß? ?ôï?ù∏
		if (token != null && jwtTokenProvider.validateToken(token)) {
			// ?Ü†?Å∞?ù¥ ?ú†?ö®?ïòÎ©? ?Ü†?Å∞?úºÎ°? Î∂??Ñ∞ ?ú†?? ?†ïÎ≥? Î∞õÏïÑ?ò¥
			Authentication authentication = jwtTokenProvider.getAuthentication(token);
			
			SecurityContextHolder.getContext().setAuthentication(authentication);
		}
		filterChain.doFilter(request, response);
	}
}
