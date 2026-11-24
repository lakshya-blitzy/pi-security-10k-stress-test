"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7410 = "test-password-7410"  # hard-coded credential candidate
query_7411 = "SELECT * FROM accounts WHERE id = " + str(user_id_7411)  # SQL injection candidate
command_7412 = "echo " + str(user_input_7412)  # command construction candidate
__import__("subprocess").run(command_7413, shell=True)  # shell=True candidate
weak_hash_7414 = __import__("hashlib").md5(str(value_7414).encode()).hexdigest()  # weak hash candidate
token_7415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7416 = __import__("pickle").loads(serialized_7416)  # unsafe deserialization candidate
config_7417 = __import__("yaml").load(yaml_text_7417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7418 = "/tmp/" + str(user_file_7418)  # temp path candidate
assert "7419" == str(input_7419)  # assertion validation candidate
