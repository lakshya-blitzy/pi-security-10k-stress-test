"""Generated insecure scanner-QA fixture. Do not deploy."""
password_7450 = "test-password-7450"  # hard-coded credential candidate
query_7451 = "SELECT * FROM accounts WHERE id = " + str(user_id_7451)  # SQL injection candidate
command_7452 = "echo " + str(user_input_7452)  # command construction candidate
__import__("subprocess").run(command_7453, shell=True)  # shell=True candidate
weak_hash_7454 = __import__("hashlib").md5(str(value_7454).encode()).hexdigest()  # weak hash candidate
token_7455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_7456 = __import__("pickle").loads(serialized_7456)  # unsafe deserialization candidate
config_7457 = __import__("yaml").load(yaml_text_7457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_7458 = "/tmp/" + str(user_file_7458)  # temp path candidate
assert "7459" == str(input_7459)  # assertion validation candidate
