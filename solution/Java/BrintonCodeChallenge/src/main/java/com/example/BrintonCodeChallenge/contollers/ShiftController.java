package com.example.BrintonCodeChallenge.contollers;

import com.example.BrintonCodeChallenge.processors.ShiftProcessor;
import com.example.BrintonCodeChallenge.vdo.ShiftDO;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping("/shifts")
public class ShiftController {

    private final ShiftProcessor processor;

    public ShiftController(ShiftProcessor processor) {
        this.processor = processor;
    }

    @PostMapping("/upload")
    public ResponseEntity<String> uploadShifts(@RequestParam("file") MultipartFile file) {
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            // Convert JSON file to list of Shift objects
            List<ShiftDO> shifts = objectMapper.readValue(file.getInputStream(),
                    objectMapper.getTypeFactory().constructCollectionType(List.class, ShiftDO.class));

            // Process shifts
            processor.processShifts(shifts);



            return ResponseEntity.ok("Shifts uploaded successfully. Total shifts: " + shifts.size());

        } catch (IOException e) {
            return ResponseEntity.badRequest().body("Error processing file: " + e.getMessage());
        }
    }
}
