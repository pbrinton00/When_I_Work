package com.example.BrintonCodeChallenge.contollers;

import com.example.BrintonCodeChallenge.services.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/employees")
public class EmployeeController {

    private final EmployeeService employeeService;

    @Autowired
    public EmployeeController(EmployeeService employeeService) {
        this.employeeService = employeeService;
    }

    /**
     * this controller is based on the object group of employee.
     * It should take 1 or many employees.
     * @Params : employee or employees IDs.
     * @Param : shifts by week.
     * @Param : Emplyee details.
     *
     * All calculations should come from the employee service.
     */
}
