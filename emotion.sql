-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 05, 2021 at 04:46 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `emotion`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `cno` int(10) NOT NULL,
  `fname` varchar(20) NOT NULL,
  `lname` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `message` varchar(50) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`cno`, `fname`, `lname`, `email`, `message`, `date`) VALUES
(12, 'Sheetal', 'Borkar', 'sheetalbborkar98@gmail.com', 'Hello, how are you?', '2021-05-30 04:00:12.059599'),
(13, 'Minty', 'Borkar', 'minty98@gmail.com', 'Hello,\r\nThis is a testing mail.\r\nHope this message', '2021-06-05 16:44:02.802783'),
(14, 'Sheetal', 'Borkar', 'sheetalbborkar98@gmail.com', 'Hello..', '2021-06-05 17:12:02.028618');

-- --------------------------------------------------------

--
-- Table structure for table `details`
--

CREATE TABLE `details` (
  `dno` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phn` varchar(11) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `details`
--

INSERT INTO `details` (`dno`, `name`, `address`, `phn`, `date`) VALUES
(1, 'Sheetal Borkar', 'Pune', '09421505680', '2021-05-30 15:37:56'),
(2, 'Pratiksha Shinde', 'Dehu', '9172399624', '2021-05-30 15:38:41'),
(3, 'Swapnil Gupta', 'Mumbai', '8839772627', '2021-05-30 15:39:16'),
(4, 'Namrata Waghmare', 'Nigdi', '8805259741', '2021-05-30 15:40:00'),
(7, 'Minty', 'pune', '09421505680', '2021-06-05 17:11:07'),
(8, 'Renuka', 'Nigdi', '98745632115', '2021-06-05 17:13:16');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `rno` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(10) NOT NULL,
  `password2` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`rno`, `name`, `email`, `password`, `password2`) VALUES
(24, 'Sheetal Badal Borkar', 'sheetal@gmail.com', '123456789', '123456789');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`cno`);

--
-- Indexes for table `details`
--
ALTER TABLE `details`
  ADD PRIMARY KEY (`dno`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`rno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `cno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `details`
--
ALTER TABLE `details`
  MODIFY `dno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `rno` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
