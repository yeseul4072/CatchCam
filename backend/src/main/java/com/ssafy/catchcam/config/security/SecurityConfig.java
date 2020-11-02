package com.ssafy.catchcam.config.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.factory.PasswordEncoderFactories;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
	@Autowired
	private JwtTokenProvider jwtTokenProvider;

	// authenticationManagerë¥? Bean ?“±ë¡í•©?‹ˆ?‹¤.
	@Bean
	@Override
	public AuthenticationManager authenticationManagerBean() throws Exception {
		return super.authenticationManagerBean();
	}

	// ?•”?˜¸?™”?— ?•„?š”?•œ PasswordEncoder ë¥? Bean ?“±ë¡í•©?‹ˆ?‹¤.
	@Bean
	public PasswordEncoder passwordEncoder() {
		return PasswordEncoderFactories.createDelegatingPasswordEncoder();
	}

	@Override
	protected void configure(HttpSecurity http) throws Exception {
		http.httpBasic().disable() // rest api ?´ë¯?ë¡? ê¸°ë³¸?„¤? • ?‚¬?š©?•ˆ?•¨. ê¸°ë³¸?„¤? •?? ë¹„ì¸ì¦ì‹œ ë¡œê·¸?¸?¼ ?™”ë©´ìœ¼ë¡? ë¦¬ë‹¤?´? ‰?Š¸ ?œ?‹¤.
				.csrf().disable() // rest api?´ë¯?ë¡? csrf ë³´ì•ˆ?´ ?•„?š”?—†?œ¼ë¯?ë¡? disableì²˜ë¦¬.
				.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS) // jwt token?œ¼ë¡? ?¸ì¦í•˜ë¯?ë¡? ?„¸?…˜??
																							// ?•„?š”?—†?œ¼ë¯?ë¡? ?ƒ?„±?•ˆ?•¨.
				.and().authorizeRequests() // ?‹¤?Œ ë¦¬í?˜ìŠ¤?Š¸?— ???•œ ?‚¬?š©ê¶Œí•œ ì²´í¬
				.antMatchers("/**/login", "/**/signup", "/**/valid/{nickname}").permitAll() // ê°??… ê´?? ¨ API?Š” ?ˆ„êµ¬ë‚˜ ? ‘ê·? ê°??Š¥
				.antMatchers("/**/count").permitAll() // ë©”ì¸ ?™”ë©´ì— ê´?? ¨?œ API ?˜?•œ ?ˆ„êµ¬ë‚˜ ? ‘ê·? ê°??Š¥
//				.antMatchers(HttpMethod.GET, "/**/lectures", "/**/lectures/count", "/**/lectures/tags", "/**/lectures/{lectureId}").permitAll()
				.antMatchers("/**/").permitAll()
				.anyRequest().hasRole("USER") // ê·¸ì™¸ ?‚˜ë¨¸ì? ?š”ì²??? ëª¨ë‘ ?¸ì¦ëœ ?šŒ?›ë§? ? ‘ê·? ê°??Š¥
				.and().addFilterBefore(new JwtAuthenticationFilter(jwtTokenProvider),
						UsernamePasswordAuthenticationFilter.class); // jwt token ?•„?„°ë¥? id/password ?¸ì¦? ?•„?„° ? „?— ?„£?Š”?‹¤
	}

	@Override // ignore check swagger resource
	public void configure(WebSecurity web) {
		web.ignoring().antMatchers("/v2/api-docs", "/swagger-resources/**", "/swagger-ui.html", "/webjars/**",
				"/swagger/**");
	}
}
