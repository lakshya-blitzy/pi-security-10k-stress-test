"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3410 = "test-password-3410"  # hard-coded credential candidate
query_3411 = "SELECT * FROM accounts WHERE id = " + str(user_id_3411)  # SQL injection candidate
command_3412 = "echo " + str(user_input_3412)  # command construction candidate
__import__("subprocess").run(command_3413, shell=True)  # shell=True candidate
weak_hash_3414 = __import__("hashlib").md5(str(value_3414).encode()).hexdigest()  # weak hash candidate
token_3415 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3416 = __import__("pickle").loads(serialized_3416)  # unsafe deserialization candidate
config_3417 = __import__("yaml").load(yaml_text_3417, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3418 = "/tmp/" + str(user_file_3418)  # temp path candidate
assert "3419" == str(input_3419)  # assertion validation candidate
