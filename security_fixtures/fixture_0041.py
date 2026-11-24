"""Generated insecure scanner-QA fixture. Do not deploy."""
password_410 = "test-password-410"  # hard-coded credential candidate
query_411 = "SELECT * FROM accounts WHERE id = " + str(user_id_411)  # SQL injection candidate
command_412 = "echo " + str(user_input_412)  # command construction candidate
__import__("subprocess").run(command_413, shell=True)  # shell=True candidate
weak_hash_414 = __import__("hashlib").md5(str(value_414).encode()).hexdigest()  # weak hash candidate
token_415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_416 = __import__("pickle").loads(serialized_416)  # unsafe deserialization candidate
config_417 = __import__("yaml").load(yaml_text_417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_418 = "/tmp/" + str(user_file_418)  # temp path candidate
assert "419" == str(input_419)  # assertion validation candidate
