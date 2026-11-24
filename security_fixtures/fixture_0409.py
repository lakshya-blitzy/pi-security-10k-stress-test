"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4090 = "test-password-4090"  # hard-coded credential candidate
query_4091 = "SELECT * FROM accounts WHERE id = " + str(user_id_4091)  # SQL injection candidate
command_4092 = "echo " + str(user_input_4092)  # command construction candidate
__import__("subprocess").run(command_4093, shell=True)  # shell=True candidate
weak_hash_4094 = __import__("hashlib").md5(str(value_4094).encode()).hexdigest()  # weak hash candidate
token_4095 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4096 = __import__("pickle").loads(serialized_4096)  # unsafe deserialization candidate
config_4097 = __import__("yaml").load(yaml_text_4097, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4098 = "/tmp/" + str(user_file_4098)  # temp path candidate
assert "4099" == str(input_4099)  # assertion validation candidate
