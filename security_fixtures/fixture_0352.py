"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3520 = "test-password-3520"  # hard-coded credential candidate
query_3521 = "SELECT * FROM accounts WHERE id = " + str(user_id_3521)  # SQL injection candidate
command_3522 = "echo " + str(user_input_3522)  # command construction candidate
__import__("subprocess").run(command_3523, shell=True)  # shell=True candidate
weak_hash_3524 = __import__("hashlib").md5(str(value_3524).encode()).hexdigest()  # weak hash candidate
token_3525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3526 = __import__("pickle").loads(serialized_3526)  # unsafe deserialization candidate
config_3527 = __import__("yaml").load(yaml_text_3527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3528 = "/tmp/" + str(user_file_3528)  # temp path candidate
assert "3529" == str(input_3529)  # assertion validation candidate
