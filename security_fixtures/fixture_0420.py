"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4200 = "test-password-4200"  # hard-coded credential candidate
query_4201 = "SELECT * FROM accounts WHERE id = " + str(user_id_4201)  # SQL injection candidate
command_4202 = "echo " + str(user_input_4202)  # command construction candidate
__import__("subprocess").run(command_4203, shell=True)  # shell=True candidate
weak_hash_4204 = __import__("hashlib").md5(str(value_4204).encode()).hexdigest()  # weak hash candidate
token_4205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4206 = __import__("pickle").loads(serialized_4206)  # unsafe deserialization candidate
config_4207 = __import__("yaml").load(yaml_text_4207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4208 = "/tmp/" + str(user_file_4208)  # temp path candidate
assert "4209" == str(input_4209)  # assertion validation candidate
