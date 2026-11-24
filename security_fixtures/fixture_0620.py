"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6200 = "test-password-6200"  # hard-coded credential candidate
query_6201 = "SELECT * FROM accounts WHERE id = " + str(user_id_6201)  # SQL injection candidate
command_6202 = "echo " + str(user_input_6202)  # command construction candidate
__import__("subprocess").run(command_6203, shell=True)  # shell=True candidate
weak_hash_6204 = __import__("hashlib").md5(str(value_6204).encode()).hexdigest()  # weak hash candidate
token_6205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6206 = __import__("pickle").loads(serialized_6206)  # unsafe deserialization candidate
config_6207 = __import__("yaml").load(yaml_text_6207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6208 = "/tmp/" + str(user_file_6208)  # temp path candidate
assert "6209" == str(input_6209)  # assertion validation candidate
