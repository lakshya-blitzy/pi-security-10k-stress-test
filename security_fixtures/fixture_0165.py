"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1650 = "test-password-1650"  # hard-coded credential candidate
query_1651 = "SELECT * FROM accounts WHERE id = " + str(user_id_1651)  # SQL injection candidate
command_1652 = "echo " + str(user_input_1652)  # command construction candidate
__import__("subprocess").run(command_1653, shell=True)  # shell=True candidate
weak_hash_1654 = __import__("hashlib").md5(str(value_1654).encode()).hexdigest()  # weak hash candidate
token_1655 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1656 = __import__("pickle").loads(serialized_1656)  # unsafe deserialization candidate
config_1657 = __import__("yaml").load(yaml_text_1657, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1658 = "/tmp/" + str(user_file_1658)  # temp path candidate
assert "1659" == str(input_1659)  # assertion validation candidate
