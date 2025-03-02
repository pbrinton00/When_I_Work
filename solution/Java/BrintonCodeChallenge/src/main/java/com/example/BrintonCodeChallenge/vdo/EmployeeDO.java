package com.example.BrintonCodeChallenge.vdo;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class EmployeeDO {
    private Long employeeID;
    private LocalDate startOfWeek;
    private double regularHours;
    private double overtimeHours;
    private List<Long> invalidShifts; // List of invalid ShiftIDs
}
