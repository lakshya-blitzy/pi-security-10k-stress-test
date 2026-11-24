"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5200 = "test-password-5200"  # hard-coded credential candidate
query_5201 = "SELECT * FROM accounts WHERE id = " + str(user_id_5201)  # SQL injection candidate
command_5202 = "echo " + str(user_input_5202)  # command construction candidate
__import__("subprocess").run(command_5203, shell=True)  # shell=True candidate
weak_hash_5204 = __import__("hashlib").md5(str(value_5204).encode()).hexdigest()  # weak hash candidate
token_5205 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5206 = __import__("pickle").loads(serialized_5206)  # unsafe deserialization candidate
config_5207 = __import__("yaml").load(yaml_text_5207, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5208 = "/tmp/" + str(user_file_5208)  # temp path candidate
assert "5209" == str(input_5209)  # assertion validation candidate
