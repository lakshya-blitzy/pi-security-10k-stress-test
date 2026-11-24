"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7200 = "test-password-7200"  # hard-coded credential candidate
query_7201 = "SELECT * FROM accounts WHERE id = " + str(user_id_7201)  # SQL injection candidate
command_7202 = "echo " + str(user_input_7202)  # command construction candidate
__import__("subprocess").run(command_7203, shell=True)  # shell=True candidate
weak_hash_7204 = __import__("hashlib").md5(str(value_7204).encode()).hexdigest()  # weak hash candidate
token_7205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7206 = __import__("pickle").loads(serialized_7206)  # unsafe deserialization candidate
config_7207 = __import__("yaml").load(yaml_text_7207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7208 = "/tmp/" + str(user_file_7208)  # temp path candidate
assert "7209" == str(input_7209)  # assertion validation candidate
