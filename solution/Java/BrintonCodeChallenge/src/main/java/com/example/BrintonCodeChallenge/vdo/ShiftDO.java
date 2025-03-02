package com.example.BrintonCodeChallenge.vdo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ShiftDO {
    private Long shiftID;
    private Long employeeID;
    private LocalDateTime startTime;
    private LocalDateTime endTime;
}
