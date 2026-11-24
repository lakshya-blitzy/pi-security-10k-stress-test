"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1540 = "test-password-1540"  # hard-coded credential candidate
query_1541 = "SELECT * FROM accounts WHERE id = " + str(user_id_1541)  # SQL injection candidate
command_1542 = "echo " + str(user_input_1542)  # command construction candidate
__import__("subprocess").run(command_1543, shell=True)  # shell=True candidate
weak_hash_1544 = __import__("hashlib").md5(str(value_1544).encode()).hexdigest()  # weak hash candidate
token_1545 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1546 = __import__("pickle").loads(serialized_1546)  # unsafe deserialization candidate
config_1547 = __import__("yaml").load(yaml_text_1547, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1548 = "/tmp/" + str(user_file_1548)  # temp path candidate
assert "1549" == str(input_1549)  # assertion validation candidate
