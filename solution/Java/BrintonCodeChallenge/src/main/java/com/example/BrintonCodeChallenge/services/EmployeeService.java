package com.example.BrintonCodeChallenge.services;

import com.example.BrintonCodeChallenge.vdo.EmployeeDO;
import org.springframework.stereotype.Service;

import java.util.Date;

@Service
public class EmployeeService {
    /**
     * Fetch employee shift data (Mocked for now).
     * @param employeeID Employee ID to fetch
     * @return Employee object with shift details
     */
    public EmployeeDO getEmployeeShiftsByWeek(Long employeeId, Date week) {
        // stubed out for now.  Need real datastore connection and retrieve
        EmployeeDO employeeDO = new EmployeeDO();
        return employeeDO;
    }
}
