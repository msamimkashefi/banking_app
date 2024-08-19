-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2024 at 01:20 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `id` int(11) NOT NULL,
  `account_number` varchar(14) NOT NULL,
  `balance` float NOT NULL,
  `account_holder` int(11) NOT NULL,
  `type` enum('current','savings','business') NOT NULL,
  `opening_time` datetime NOT NULL,
  `account_status` enum('active','deactive','suspended') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`id`, `account_number`, `balance`, `account_holder`, `type`, `opening_time`, `account_status`) VALUES
(1, '10039585488121', 8355.23, 9, 'current', '2024-08-18 14:08:09', 'active'),
(2, '10039585488122', 124.92, 15, 'current', '2024-08-18 14:08:09', 'active'),
(3, '10039585488123', 2430, 9, 'current', '2024-08-18 16:46:08', 'active'),
(5, '10039585488124', 112, 9, 'current', '2024-08-18 16:54:38', 'active'),
(6, '10039585488125', 3253, 15, 'savings', '2024-08-18 16:55:50', 'active'),
(7, '10039585488126', 294, 16, 'business', '2024-08-18 16:57:55', 'active'),
(8, '10039585488127', 0, 15, 'current', '2024-08-18 16:58:51', 'active'),
(9, '10039585488128', 223, 17, 'savings', '2024-08-18 17:01:57', 'active'),
(10, '10039585488129', 434, 17, 'business', '2024-08-18 17:09:39', 'active'),
(11, '10039585488130', 9144, 22, 'savings', '2024-08-19 12:26:09', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `tr_number` varchar(15) NOT NULL,
  `tr_amount` float NOT NULL,
  `tr_time` datetime NOT NULL,
  `source_account` int(11) NOT NULL,
  `destination_account` int(11) NOT NULL,
  `transfered_by` int(11) DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `tr_number`, `tr_amount`, `tr_time`, `source_account`, `destination_account`, `transfered_by`, `note`) VALUES
(1, '1', 10, '2024-08-18 23:55:35', 1, 3, NULL, 'Some Note'),
(2, '2', 10, '2024-08-18 23:56:08', 3, 1, NULL, 'Some Note'),
(3, '3', 20, '2024-08-19 12:23:35', 7, 9, NULL, 'Mach\'s gut!'),
(4, '4', 90, '2024-08-19 12:29:53', 11, 9, NULL, 'Strom'),
(5, '5', 70, '2024-08-19 12:31:51', 3, 2, NULL, 'SDKLFJ#*#(2'),
(6, '6', 14, '2024-08-19 12:33:49', 1, 9, NULL, '&*^*^$%^%$'),
(7, '7', 13, '2024-08-19 12:34:37', 1, 10, NULL, 'Good Luck!');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `password` varchar(100) NOT NULL,
  `created_by` int(11) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `type` enum('admin','ac_holder') NOT NULL,
  `birth_date` date DEFAULT NULL,
  `nationality` varchar(20) DEFAULT NULL,
  `current_address` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `email`, `phone`, `password`, `created_by`, `created_at`, `type`, `birth_date`, `nationality`, `current_address`) VALUES
(9, 'Ahmad', 'Ahmadi', 'ahmad@gmail.com', '238923894', '827ccb0eea8a706c4c34a16891f84e7b', NULL, '2024-08-08 17:24:00', 'ac_holder', '2024-07-30', 'Austria', 'Kabul'),
(15, 'Fardin', 'Kamgar', 'fardeen@gmail.com', '82393091002', '827ccb0eea8a706c4c34a16891f84e7b', NULL, '2024-08-18 00:21:25', 'ac_holder', '2024-06-13', 'American Samoa', 'Mazar'),
(16, 'Noman', 'Habib', 'noman@gmail.com', '2988924891', '827ccb0eea8a706c4c34a16891f84e7b', NULL, '2024-08-18 00:24:22', 'ac_holder', '2024-08-01', 'Antarctica', 'Badakhshan'),
(17, 'shabnam', 'Qeech', 'shabnam@gmail.com', '015231829844', '827ccb0eea8a706c4c34a16891f84e7b', NULL, '2024-08-18 00:28:16', 'ac_holder', '2024-08-01', 'Cape Verde', 'Parwan'),
(21, 'Raiko', 'Costa', 'raiko@gmail.com', '+49152153423', '827ccb0eea8a706c4c34a16891f84e7b', NULL, '2024-08-18 17:30:21', 'ac_holder', '1976-01-28', 'Germany', 'Kiel. XYZ'),
(22, 'Sabah', 'Volkanovski', 'sabah@gmail.com', '+12994322123', '827ccb0eea8a706c4c34a16891f84e7b', NULL, '2024-08-19 12:25:45', 'ac_holder', '1996-02-29', 'Australia', 'Melborn');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `account_number` (`account_number`),
  ADD KEY `account_holder` (`account_holder`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `number` (`tr_number`),
  ADD KEY `source_account` (`source_account`),
  ADD KEY `transfered_by` (`transfered_by`),
  ADD KEY `destination_account` (`destination_account`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `account`
--
ALTER TABLE `account`
  ADD CONSTRAINT `account_ibfk_1` FOREIGN KEY (`account_holder`) REFERENCES `user` (`id`);

--
-- Constraints for table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`source_account`) REFERENCES `account` (`id`),
  ADD CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`transfered_by`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `transaction_ibfk_3` FOREIGN KEY (`destination_account`) REFERENCES `account` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
