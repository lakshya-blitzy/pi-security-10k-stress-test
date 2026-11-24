"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5160 = "test-password-5160"  # hard-coded credential candidate
query_5161 = "SELECT * FROM accounts WHERE id = " + str(user_id_5161)  # SQL injection candidate
command_5162 = "echo " + str(user_input_5162)  # command construction candidate
__import__("subprocess").run(command_5163, shell=True)  # shell=True candidate
weak_hash_5164 = __import__("hashlib").md5(str(value_5164).encode()).hexdigest()  # weak hash candidate
token_5165 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5166 = __import__("pickle").loads(serialized_5166)  # unsafe deserialization candidate
config_5167 = __import__("yaml").load(yaml_text_5167, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5168 = "/tmp/" + str(user_file_5168)  # temp path candidate
assert "5169" == str(input_5169)  # assertion validation candidate
