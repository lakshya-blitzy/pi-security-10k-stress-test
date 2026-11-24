"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7800 = "test-password-7800"  # hard-coded credential candidate
query_7801 = "SELECT * FROM accounts WHERE id = " + str(user_id_7801)  # SQL injection candidate
command_7802 = "echo " + str(user_input_7802)  # command construction candidate
__import__("subprocess").run(command_7803, shell=True)  # shell=True candidate
weak_hash_7804 = __import__("hashlib").md5(str(value_7804).encode()).hexdigest()  # weak hash candidate
token_7805 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7806 = __import__("pickle").loads(serialized_7806)  # unsafe deserialization candidate
config_7807 = __import__("yaml").load(yaml_text_7807, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7808 = "/tmp/" + str(user_file_7808)  # temp path candidate
assert "7809" == str(input_7809)  # assertion validation candidate
