"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4410 = "test-password-4410"  # hard-coded credential candidate
query_4411 = "SELECT * FROM accounts WHERE id = " + str(user_id_4411)  # SQL injection candidate
command_4412 = "echo " + str(user_input_4412)  # command construction candidate
__import__("subprocess").run(command_4413, shell=True)  # shell=True candidate
weak_hash_4414 = __import__("hashlib").md5(str(value_4414).encode()).hexdigest()  # weak hash candidate
token_4415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4416 = __import__("pickle").loads(serialized_4416)  # unsafe deserialization candidate
config_4417 = __import__("yaml").load(yaml_text_4417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4418 = "/tmp/" + str(user_file_4418)  # temp path candidate
assert "4419" == str(input_4419)  # assertion validation candidate
