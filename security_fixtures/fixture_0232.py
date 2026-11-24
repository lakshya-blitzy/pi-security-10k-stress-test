"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2320 = "test-password-2320"  # hard-coded credential candidate
query_2321 = "SELECT * FROM accounts WHERE id = " + str(user_id_2321)  # SQL injection candidate
command_2322 = "echo " + str(user_input_2322)  # command construction candidate
__import__("subprocess").run(command_2323, shell=True)  # shell=True candidate
weak_hash_2324 = __import__("hashlib").md5(str(value_2324).encode()).hexdigest()  # weak hash candidate
token_2325 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2326 = __import__("pickle").loads(serialized_2326)  # unsafe deserialization candidate
config_2327 = __import__("yaml").load(yaml_text_2327, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2328 = "/tmp/" + str(user_file_2328)  # temp path candidate
assert "2329" == str(input_2329)  # assertion validation candidate
