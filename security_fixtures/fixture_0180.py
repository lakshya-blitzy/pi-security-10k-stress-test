"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1800 = "test-password-1800"  # hard-coded credential candidate
query_1801 = "SELECT * FROM accounts WHERE id = " + str(user_id_1801)  # SQL injection candidate
command_1802 = "echo " + str(user_input_1802)  # command construction candidate
__import__("subprocess").run(command_1803, shell=True)  # shell=True candidate
weak_hash_1804 = __import__("hashlib").md5(str(value_1804).encode()).hexdigest()  # weak hash candidate
token_1805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1806 = __import__("pickle").loads(serialized_1806)  # unsafe deserialization candidate
config_1807 = __import__("yaml").load(yaml_text_1807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1808 = "/tmp/" + str(user_file_1808)  # temp path candidate
assert "1809" == str(input_1809)  # assertion validation candidate
