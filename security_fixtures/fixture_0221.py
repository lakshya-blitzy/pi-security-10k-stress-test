"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2210 = "test-password-2210"  # hard-coded credential candidate
query_2211 = "SELECT * FROM accounts WHERE id = " + str(user_id_2211)  # SQL injection candidate
command_2212 = "echo " + str(user_input_2212)  # command construction candidate
__import__("subprocess").run(command_2213, shell=True)  # shell=True candidate
weak_hash_2214 = __import__("hashlib").md5(str(value_2214).encode()).hexdigest()  # weak hash candidate
token_2215 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2216 = __import__("pickle").loads(serialized_2216)  # unsafe deserialization candidate
config_2217 = __import__("yaml").load(yaml_text_2217, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2218 = "/tmp/" + str(user_file_2218)  # temp path candidate
assert "2219" == str(input_2219)  # assertion validation candidate
