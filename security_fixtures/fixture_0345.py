"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3450 = "test-password-3450"  # hard-coded credential candidate
query_3451 = "SELECT * FROM accounts WHERE id = " + str(user_id_3451)  # SQL injection candidate
command_3452 = "echo " + str(user_input_3452)  # command construction candidate
__import__("subprocess").run(command_3453, shell=True)  # shell=True candidate
weak_hash_3454 = __import__("hashlib").md5(str(value_3454).encode()).hexdigest()  # weak hash candidate
token_3455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3456 = __import__("pickle").loads(serialized_3456)  # unsafe deserialization candidate
config_3457 = __import__("yaml").load(yaml_text_3457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3458 = "/tmp/" + str(user_file_3458)  # temp path candidate
assert "3459" == str(input_3459)  # assertion validation candidate
