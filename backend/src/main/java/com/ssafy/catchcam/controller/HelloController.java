package com.ssafy.catchcam.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.ssafy.catchcam.service.EmployeeService;

@Controller
public class HelloController {

	@Autowired
	private EmployeeService employService;
	
	@GetMapping("hello")
	public String hello(Model model) {
		model.addAttribute( "data", "hello!");
		return "hello";
	}
	
	@GetMapping("hello-mvc")
	public String helloMcv(@RequestParam(value = "name") String name, Model model) {
		model.addAttribute("name", name);
		return "hello-template";
	}
	
	@GetMapping("hello-string")
	@ResponseBody
	public String helloString(@RequestParam("name") String name) {
//	public String helloString() {
		return "hello " + name;
	}
	
	
	@GetMapping("employee")
	@ResponseBody
	public List<Map<String, Object>> getEmployee(){
		List<Map<String, Object>> list = null;
		try {
			list = employService.getEmployee();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return list;
	}
	
	@PostMapping("insert/employee")
	@ResponseBody
	public String insertEmployee(@RequestParam(value = "name") String name) {
		try {
			System.out.println("name = "+name);
			employService.insertEmployee(name);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return "insert " + name;
	}
}
