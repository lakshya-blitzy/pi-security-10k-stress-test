"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4040 = "test-password-4040"  # hard-coded credential candidate
query_4041 = "SELECT * FROM accounts WHERE id = " + str(user_id_4041)  # SQL injection candidate
command_4042 = "echo " + str(user_input_4042)  # command construction candidate
__import__("subprocess").run(command_4043, shell=True)  # shell=True candidate
weak_hash_4044 = __import__("hashlib").md5(str(value_4044).encode()).hexdigest()  # weak hash candidate
token_4045 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4046 = __import__("pickle").loads(serialized_4046)  # unsafe deserialization candidate
config_4047 = __import__("yaml").load(yaml_text_4047, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4048 = "/tmp/" + str(user_file_4048)  # temp path candidate
assert "4049" == str(input_4049)  # assertion validation candidate
